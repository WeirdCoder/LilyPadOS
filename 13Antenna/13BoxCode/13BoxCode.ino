//-------------------------------------MAGNETOMETER---------------------------//
//-------------------------------------MAGNETOMETER---------------------------//
//-------------------------------------MAGNETOMETER---------------------------//
//-------------------------------------MAGNETOMETER---------------------------//
//-------------------------------------MAGNETOMETER---------------------------//
//-------------------------------------MAGNETOMETER---------------------------//
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

void getMagStats(void) {
  //Reference this to the code in the magsensor code
  //new sensor event
  sensors_event_t event;
  mag.getEvent(&event);
  // Display the output from the magnetometer
  Serial.print("X: "); Serial.print(event.magnetic.x); Serial.print("  ");
  Serial.print("Y: "); Serial.print(event.magnetic.y); Serial.print("  ");
  Serial.print("Z: "); Serial.print(event.magnetic.z); Serial.print("  ");Serial.println("uT");
  float heading = atan2(event.magnetic.y, event.magnetic.x);
  float declinationAngle = 0.22;
  heading += declinationAngle;
  
  // Correct for when signs are reversed.
  if(heading < 0)
    heading += 2*PI;
    
  // Check for wrap due to addition of declination.
  if(heading > 2*PI)
    heading -= 2*PI;
  float headingDegrees = heading * 180/M_PI; 
  
  Serial.print("Heading (degrees): "); Serial.println(headingDegrees);
}

//------------------------------------GPS------------------------------------------//
//------------------------------------GPS------------------------------------------//
//------------------------------------GPS------------------------------------------//
//------------------------------------GPS------------------------------------------//
//------------------------------------GPS------------------------------------------//
//------------------------------------GPS------------------------------------------//
#include <SoftwareSerial.h>
#include <TinyGPS.h>

TinyGPS gps;
SoftwareSerial ss(4, 3);

void getGPSstats() {
  bool newData = false;
  unsigned long chars;
  unsigned short sentences, failed;
  
  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    while (ss.available())
    {
      char c = ss.read();
      // Serial.write(c); // uncomment this line if you want to see the GPS data flowing
      if (gps.encode(c)) // Did a new valid sentence come in?
        newData = true;
    }
    if (newData)
  {
    float flat, flon;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);
    Serial.print("LAT=");
    Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    Serial.print(" LON=");
    Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial.print(" SAT=");
    Serial.print(gps.satellites() == TinyGPS::GPS_INVALID_SATELLITES ? 0 : gps.satellites());
    Serial.print(" PREC=");
    Serial.print(gps.hdop() == TinyGPS::GPS_INVALID_HDOP ? 0 : gps.hdop());
  }
  
  gps.stats(&chars, &sentences, &failed);
  Serial.print(" CHARS=");
  Serial.print(chars);
  Serial.print(" SENTENCES=");
  Serial.print(sentences);
  Serial.print(" CSUM ERR=");
  Serial.println(failed);
  if (chars == 0)
    Serial.println("** No characters received from GPS: check wiring **");
  }
}

//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//
//------------------------------------WIND 1---------------------------------//

#define analogPinForRV    1 
#define analogPinForTMP   0

const float zeroWindAdjustment =  .2; // negative numbers yield smaller wind speeds and vice versa.

int TMP_Therm_ADunits;  //temp termistor value from wind sensor
float RV_Wind_ADunits;    //RV output from wind sensor 
float RV_Wind_Volts;
unsigned long lastMillis;
int TempCtimes100;
float zeroWind_ADunits;
float zeroWind_volts;
float WindSpeed_MPH;

void getWindData_1(){
if (millis() - lastMillis > 200){      // read every 200 ms - printing slows this down further
    
    TMP_Therm_ADunits = analogRead(analogPinForTMP);
    RV_Wind_ADunits = analogRead(analogPinForRV);
    RV_Wind_Volts = (RV_Wind_ADunits *  0.0048828125);

    // these are all derived from regressions from raw data as such they depend on a lot of experimental factors
    // such as accuracy of temp sensors, and voltage at the actual wind sensor, (wire losses) which were unaccouted for.
    TempCtimes100 = (0.005 *((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits)) - (16.862 * (float)TMP_Therm_ADunits) + 9075.4;  

    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + 47.172;  //  13.0C  553  482.39

    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;  

    // This from a regression from data in the form of 
    // Vraw = V0 + b * WindSpeed ^ c
    // V0 is zero wind at a particular temperature
    // The constants b and c were determined by some Excel wrangling with the solver.
    
   WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265);   
   
    Serial.print("  TMP volts ");
    Serial.print(TMP_Therm_ADunits * 0.0048828125);
    
    Serial.print(" RV volts ");
    Serial.print((float)RV_Wind_Volts);

    Serial.print("\t  TempC*100 ");
    Serial.print(TempCtimes100 );

    Serial.print("   ZeroWind volts ");
    Serial.print(zeroWind_volts);

    Serial.print("   WindSpeed MPH ");
    Serial.println((float)WindSpeed_MPH);
    lastMillis = millis();    
  } 
  
}


//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//
//------------------------------------WIND 2---------------------------------//

#define analogPinForRV_0    3 
#define analogPinForTMP_0   2

const float zeroWindAdjustment_0 =  .2; // negative numbers yield smaller wind speeds and vice versa.

int TMP_Therm_ADunits_0;  //temp termistor value from wind sensor
float RV_Wind_ADunits_0;    //RV output from wind sensor 
float RV_Wind_Volts_0;
unsigned long lastMillis_0;
int TempCtimes100_0;
float zeroWind_ADunits_0;
float zeroWind_volts_0;
float WindSpeed_MPH_0;

void getWindData_2() {
if (millis() - lastMillis > 200){      // read every 200 ms - printing slows this down further
    
    TMP_Therm_ADunits_0 = analogRead(analogPinForTMP_0);
    RV_Wind_ADunits_0 = analogRead(analogPinForRV_0);
//    Serial.println(TMP_Therm_ADunits_0);
//    Serial.println(RV_Wind_ADunits_0);
    RV_Wind_Volts_0 = (RV_Wind_ADunits_0 *  0.0048828125);

    // these are all derived from regressions from raw data as such they depend on a lot of experimental factors
    // such as accuracy of temp sensors, and voltage at the actual wind sensor, (wire losses) which were unaccouted for.
    TempCtimes100_0 = (0.005 *((float)TMP_Therm_ADunits_0 * (float)TMP_Therm_ADunits_0)) - (16.862 * (float)TMP_Therm_ADunits_0) + 9075.4;  

    zeroWind_ADunits_0 = -0.0006*((float)TMP_Therm_ADunits_0 * (float)TMP_Therm_ADunits_0) + 1.0727 * (float)TMP_Therm_ADunits_0 + 47.172;  //  13.0C  553  482.39

    zeroWind_volts_0 = (zeroWind_ADunits_0 * 0.0048828125) - zeroWindAdjustment_0;  

    // This from a regression from data in the form of 
    // Vraw = V0 + b * WindSpeed ^ c
    // V0 is zero wind at a particular temperature
    // The constants b and c were determined by some Excel wrangling with the solver.
    
   WindSpeed_MPH_0 =  pow(((RV_Wind_Volts_0 - zeroWind_volts_0) /.2300) , 2.7265);   
   
    Serial.print("  TMP volts 2: ");
    Serial.print(TMP_Therm_ADunits_0 * 0.0048828125);
    
    Serial.print(" RV volts 2: ");
    Serial.print((float)RV_Wind_Volts_0);

    Serial.print("\t  TempC*100 2: ");
    Serial.print(TempCtimes100_0 );

    Serial.print("   ZeroWind volts 2: ");
    Serial.print(zeroWind_volts_0);

    Serial.print("   WindSpeed MPH 2: ");
    Serial.println((float)WindSpeed_MPH_0);
    lastMillis = millis();    
  } 
}
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
//------------------------------------SETUP----------------------------------------//
void setup() {
  Serial.begin(9600);
  
  if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
  Serial.println("The magnetometer has been connected successfully!");
  delay(1000);
  
  ss.begin(4800);
  Serial.println("The GPS has been successfully connected, though no fix guaranteed");
  delay(1000);
  
  //below is not required
  //pinMode(A2, INPUT);
  //pinMode(A3, INPUT);
  //digitalWrite(A3, LOW);
  Serial.println("First wind sensor successfully connected");
  delay(1000);
  Serial.println("Second wind sensor successfully connected");
  delay(1000);
  
  
  
}

//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
//------------------------------------LOOP-----------------------------------------//
void loop() {
  getMagStats(); // get the stats for the magnetometer
  delay(500);
  //getGPSstats();
  //delay(10);
  //getWindData_1();
  //delay(10);
  //getWindData_2();
  //delay(1000);
}
