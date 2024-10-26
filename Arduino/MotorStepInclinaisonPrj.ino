/* Fichiers Includes (librairies) =================================================== */
#include <Arduino.h>
#include <SerialMenuCmd.h>

/* macros ============================================================== */

/** Declaration of operating mode. */
#define DEBUG 1         ///< The mode of operation; 0 = normal, 1 = debug.

#define LedOnBoard 13

#define pinMot_EN 10    ///< Interface pin with stepper Motor : Enable
#define pinMot_DIR 9    ///< Interface pin with stepper Motor : Direction
#define pinMot_Step 8   ///< Interface pin with stepper Motor : Step




/* Types ============================================================== */

/* Classes (instantiation) =============================================================== */
SerialMenuCmd SMC;

/* Variables =================================================== */

uint16_t loopDelayMs = 100;
bool AuthMot = 0;
int DirMot = 0;
uint16_t NbStep = 0;


/* Function Prototype(s) ====================================================================================== */
/**
 * @brief System malfunction is indicated by the led, it flash to form the
 *        morse message "SOS"
 */
void LedInfoUserPanic(void);



/* Structure list of command ================================================================================== */
tMenuCmdTxt txt1_DisplayMenu[] ="? - Menu";
tMenuCmdTxt txt2_NbStep[] ="n - Number of steps (1000 steps -> 10 mm)";
tMenuCmdTxt txt3_MovForward[] ="f - Forward movement";
tMenuCmdTxt txt4_MovReverse[] ="r - Move backwards";
//tMenuCmdTxt txt5_SensorCalibration[] ="c - force sensor calibration";
tMenuCmdTxt txt6_DispParam[] ="p - display parameters";
tMenuCmdTxt txt7_SecAuthorizedMov[] ="A - Authorisation to move";
tMenuCmdTxt txt8_GoToParam[] ="g - movement according to parameters";
//tMenuCmdTxt txt9_MeasSensor[] ="m - force sensor measurement";
tMenuCmdTxt txt10_Experimentation[] ="e - Experimentation sequence";

// Declaration text of prompt
tMenuCmdTxt txt_Prompt[] = "User";


// Prototype of function which are callback by the library
void cmd1_DisplayMenu(void);
void cmd2_DefNbStep(void);
void cmd3_DefSensForward(void);
void cmd4_DefSensReverse(void);
//void cmd5_SensorCalibration(void);
void cmd6_DispParam(void);
void cmd7_SecAuthorizedMov(void);
void cmd8_GoToParam(void);
//void cmd9_MeasSensor(void);
void cmd10_Experimentation(void);

// Initialization of structure
// type of data
// array sMenuTxt, code character , function   (Reminder the code character must be printable character)
stMenuCmd list[] = {
    {txt1_DisplayMenu, '?', cmd1_DisplayMenu},
    {txt2_NbStep, 'n', cmd2_DefNbStep},
    {txt3_MovForward, 'f', cmd3_DefSensForward},
    {txt4_MovReverse, 'r', cmd4_DefSensReverse},
//    {txt5_SensorCalibration,'c', cmd5_SensorCalibration},
    {txt6_DispParam,'p', cmd6_DispParam},
    {txt7_SecAuthorizedMov,'A', cmd7_SecAuthorizedMov},
    {txt8_GoToParam,'g', cmd8_GoToParam},
//    {txt9_MeasSensor,'m', cmd9_MeasSensor},
    {txt10_Experimentation,'e', cmd10_Experimentation}
    };

// NbCmds contains the number of command
#define NbCmds sizeof(list) / sizeof(stMenuCmd)

/*==============================================================================================================*/
/*=================== setup and loop functions implementation ==================================================*/
/*==============================================================================================================*/
void setup()
{
  // Initialise the serial bus (baudrate to be set on the computer)
  Serial.begin(115200);

  //GPIO configuration for stepper motor control
  pinMode(pinMot_EN, OUTPUT);
  pinMode(pinMot_DIR, OUTPUT);
  pinMode(pinMot_Step, OUTPUT);
  //pinMode(pinICE, INPUT);

  //Inhibit trolley control
  digitalWrite(pinMot_EN, HIGH);

  //Initialise variables
  AuthMot = 1;
  DirMot = -1;
  NbStep = 3200;

/**
   * @brief init. Common line interface for dialog between user en system by Serial port com.
   */
  if (SMC.begin(list, NbCmds, txt_Prompt) == false)
  {
    // If the initialization fails, the system informs the user via the
    // led: panic mode, led flashes in Morse code the letters "SOS"
    while (true)
    {
      // disp info PB menu cmd
      LedInfoUserPanic();
    }
  }
  // show menu and give to user the prompt
  SMC.ShowMenu();
  SMC.giveCmdPrompt();

}


void loop()
{

  uint8_t CmdCode;

  /**
   * @brief management of the interaction between the system and the user.
   * The "UserRequest" menbre function analyzes the characters transmitted by the user.
   * If an command code is identified, its number is returned (return 0 if no command). This
   * function is not blocking, it stores the intermediate data between 2 calls.
   */
  CmdCode = SMC.UserRequest();

  // possible pre-treatment here

  /**
   * @brief Execute Command
   * if a command code is returned, the system executes the corresponding command.
   * To do this, it uses the "OpsCallback" member function. this function receives
   * the command code parameter
   *
   * @note In this way, it is possible to carry out a preprocessing and postprocessing
   */
  if (CmdCode != 0)
  {
    SMC.ExeCommand(CmdCode);
  }

  // Led State Change to indicate to the user that the system is OK
  // Minnimum delay : 100ms
  digitalWrite(LedOnBoard, !digitalRead(LedOnBoard));
  delay(100);
}


/*==============================================================================================================*/
/*==================== Application's functions implementation ==================================================*/
/*==============================================================================================================*/

/**
 * @fn Flash led on-board in morse code
 */
void LedInfoUserPanic(void)
{
  /**
   * @brief Timing Morse
   * Letter S -> 3 dot (short mark)
   * Letter O -> 3 dash (long mark)
   * 1 dot => 1 unit time
   * 1 dash => 3 units time
   * 1 intra-character space => 1 units time
   * 1 inter-character space => 3 units time
   * 1 word space => 7 untis time
   *
   */

  /// letter S -> 3 dots
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(600); // inter-character space

  /// Letter O -> 3 dash
  digitalWrite(LedOnBoard, HIGH);
  delay(600);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(600);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(600);
  digitalWrite(LedOnBoard, LOW);
  delay(600); // inter-character space

  /// letter S -> 3 dots
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(200); // intra-chacracter
  digitalWrite(LedOnBoard, HIGH);
  delay(200);
  digitalWrite(LedOnBoard, LOW);
  delay(1400); // word space
}


void cmd1_DisplayMenu(void)
{
  SMC.ShowMenu();
  SMC.giveCmdPrompt();
}


void cmd2_DefNbStep(void)
{
String aValue = "! enter the number of steps to be taken (1000 steps -> 10 mm)";

  Serial.println(F(""));
  if(SMC.getStrValue(aValue) == true) {
    Serial.println(F(""));
    Serial.print(F("Nb steps = "));
    NbStep = atoi(aValue.c_str());
    Serial.println(NbStep);
  }
  else{
    NbStep = 0; //In this case, parametr is reset for security reason
  }
  Serial.println(F(""));
  SMC.giveCmdPrompt();
}


void cmd3_DefSensForward(void)
{
  DirMot = 1;
  Serial.println(F(""));
  Serial.println(F("Forward movement of the motor"));
  SMC.giveCmdPrompt();
}


void cmd4_DefSensReverse(void)
{
  DirMot = -1;
  Serial.println(F(""));
  Serial.println(F("Moving the motor backwards"));
  SMC.giveCmdPrompt();
}





void cmd6_DispParam(void)
{
  Serial.println(F(""));
  Serial.println(F("Parameters list : "));

  Serial.print(F(" - Movement authorisation : "));
  if (AuthMot == 1)
    Serial.println(F("Validated"));
  else
    Serial.println(F("Inhibited"));

  Serial.print(F(" - Direction of movement : "));
  if (DirMot == 1)
    Serial.println(F("Forward"));
  else if (DirMot == -1)
    Serial.println(F("Backward"));
  else
    Serial.println(F("Undefined"));

  Serial.print(F(" - Number of steps to be taken (1000 steps => 10 mm) : "));
  if ((NbStep > 0) && (NbStep <= 30000))
    Serial.println(NbStep);
  else
    Serial.println(F("Undefined"));

  Serial.println(F(""));
  SMC.giveCmdPrompt();
}



void cmd7_SecAuthorizedMov(void)
{
  AuthMot = true;
}



void cmd8_GoToParam(void)
{
 bool fCheckConf = true;
 uint16_t ui16Step;

  if ((NbStep < 1) || (NbStep > 30000))
    fCheckConf = false;

  if ((DirMot != 1) && (DirMot != -1))
    fCheckConf = false;

  if (AuthMot == false)
    fCheckConf = false;

  Serial.println(F(""));

  //Checking parameters
  if (fCheckConf == false)
  {
    Serial.println(F("Wrong carriage movement parameter(s)"));
    SMC.giveCmdPrompt();
    return;
  }

  Serial.println(F("Fire Go potato"));

  if (DirMot == 1)
    digitalWrite(pinMot_DIR, LOW);
  else
    digitalWrite(pinMot_DIR, HIGH);

  digitalWrite(pinMot_Step, LOW);
  digitalWrite(pinMot_EN, LOW);

  for (ui16Step = 0; ui16Step < NbStep; ui16Step++)
  {
    digitalWrite(pinMot_EN, LOW);
    delayMicroseconds(1000);
    digitalWrite(pinMot_Step, HIGH);
    delayMicroseconds(1000);
    digitalWrite(pinMot_Step, LOW);
    delayMicroseconds(2000);
    digitalWrite(pinMot_EN, HIGH);
    delayMicroseconds(5000);
    if (Serial.available()){
      AuthMot = false;
      break;
      
    }
  }

  digitalWrite(pinMot_EN, HIGH);

  if (AuthMot == 1)
    Serial.println(F("Movement interrupted, safety activated"));

  Serial.println(F("End of movement"));
  SMC.giveCmdPrompt();
}



void cmd10_Experimentation(void)
{

}
