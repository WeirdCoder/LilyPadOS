// MAGNETOMETER
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>
Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

// wiring for magnetometer:
// red: 5V
// black: gnd
// yellow: A4
// green: A5
void get_mag(void) {
  // for calibrating; prints the x, y, z values of the magnetometer
  sensors_event_t event;
  mag.getEvent(&event);
  Serial.print("X= "); Serial.print(event.magnetic.x);
  Serial.print("  Y= "); Serial.print(event.magnetic.y);
  Serial.print("  Z= "); Serial.println(event.magnetic.z);
}

float get_heading(void) {
  // get the heading readout from the magnetometer
  if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
  
  sensors_event_t event;  
  mag.getEvent(&event);
  float heading = atan2(event.magnetic.y, event.magnetic.x);
  float declinationAngle = 0.22;
  heading += declinationAngle;
  if(heading < 0)
    heading += 2*PI;
    
  // Check for wrap due to addition of declination.
  if(heading > 2*PI)
    heading -= 2*PI;
  float headingDegrees = heading * 180/M_PI; 
  return headingDegrees;
//  Serial.print(headingDegrees);
}

// WIND DATA
#define analogPinForRV_1    1 //green - wind sensor 1
#define analogPinForTMP_1   0 //white - wind sensor 1
#define analogPinForRV_2    3 //green - wind sensor 2 
#define analogPinForTMP_2   2 //white - wind sensor 2

//possible
#define analogPinForRV_3   4  
#define analogPinForRV_4   5
#define analogPinForTMP_3  6
#define analogPinForTMP_4  7

// defining constants
const float zeroWindAdjustment =  .2; // negative numbers yield smaller wind speeds and vice versa.

int TMP_Therm_ADunits;  //temp termistor value from wind sensor
float RV_Wind_ADunits;    //RV output from wind sensor 
float RV_Wind_Volts;
unsigned long lastMillis;
int TempCtimes100;
float zeroWind_ADunits;
float zeroWind_volts;
float WindSpeed_MPH;

float get_anem(int sensor) {
  // used for getting the wind data from each wind sensor;
  if (sensor == 1) {
    TMP_Therm_ADunits = analogRead(analogPinForTMP_1);
    RV_Wind_ADunits = analogRead(analogPinForRV_1);
    RV_Wind_Volts = (RV_Wind_ADunits * 0.0048828125);
    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + (47.172);  //  13.0C  553  482.39
    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;
    WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265); //final answer
  }
  else if (sensor == 2) {
    TMP_Therm_ADunits = analogRead(analogPinForTMP_2);
    RV_Wind_ADunits = analogRead(analogPinForRV_2);
    RV_Wind_Volts = (RV_Wind_ADunits * 0.0048828125);
    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + (47.172);
    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;  
    WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265); //final answer
  }
  else if (sensor == 3){
    TMP_Therm_ADunits = analogRead(analogPinForTMP_3);
    RV_Wind_ADunits = analogRead(analogPinForRV_3);
    RV_Wind_Volts = (RV_Wind_ADunits * 0.0048828125);
    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + (47.172); 
    //zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + 47.172;  //  13.0C  553  482.39
    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;  
    WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265); //final answer
  }
  else {
    TMP_Therm_ADunits = analogRead(analogPinForTMP_4);
    RV_Wind_ADunits = analogRead(analogPinForRV_4);
    RV_Wind_Volts = (RV_Wind_ADunits * 0.0048828125);
    zeroWind_ADunits = -0.0006*((float)TMP_Therm_ADunits * (float)TMP_Therm_ADunits) + 1.0727 * (float)TMP_Therm_ADunits + (47.172);  //  13.0C  553  482.39
    zeroWind_volts = (zeroWind_ADunits * 0.0048828125) - zeroWindAdjustment;  
    WindSpeed_MPH =  pow(((RV_Wind_Volts - zeroWind_volts) /.2300) , 2.7265); //final answer
  }
  return WindSpeed_MPH * .868976;
}

float get_wind() {
  // this is what we will send to the airplane. Still in the making
  float wind_x;
  float wind_y;
  float heading;
  float wind_mag;
  float wind_dir;
  
  if (get_anem(1) > get_anem(2)) {
    wind_x = get_anem(1);
  }
  else {
    wind_x = -get_anem(2);
  }
  
  if (get_anem(3) > get_anem(4)) {
    wind_y = get_anem(3);
  }
  else {
    wind_y = -get_anem(4);
  }
  
  wind_mag = sqrt(pow(wind_x,2) + pow(wind_y,2));
  wind_dir = atan2(wind_y , wind_x);
  
  if(wind_dir < 0)
    wind_dir += 2*PI;
    
  // Check for wrap due to addition of declination.
  if(wind_dir > 2*PI)
    wind_dir -= 2*PI;
  wind_dir = wind_dir * 180/PI; 
  
  Serial.print(wind_mag,6); Serial.print(","); Serial.print(wind_dir,6); Serial.print(",");
}

//GPS Data
#include <SoftwareSerial.h>
#include <TinyGPS.h>

TinyGPS gps;
SoftwareSerial ss(4, 3);
// gps wiring
// black: gnd
// red :5V
// white: D4
// yellow: D3

void get_gps() {
  bool newData = false;
  unsigned long chars;
  unsigned short sentences, failed;
  
  int time = 100;
  for (unsigned long start = millis(); millis() - start < time;)
  {
    while (ss.available())
    {
      char c = ss.read();
      //Serial.write(c); // uncomment this line if you want to see the GPS data flowing
     if (gps.encode(c)) // Did a new valid sentence come in?
        newData = true;
    }
  }
  if (newData)
  {
    float flat, flon;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);
    Serial.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    Serial.print(',');
    //delay(100);
    Serial.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial.print(',');
//    Serial.print(" SAT=");
//    Serial.print(gps.satellites() == TinyGPS::GPS_INVALID_SATELLITES ? 0 : gps.satellites());
//    Serial.print(" PREC=");
//    Serial.print(gps.hdop() == TinyGPS::GPS_INVALID_HDOP ? 0 : gps.hdop());
  }
  else {
    Serial.print(42.358496,6); Serial.print(","); Serial.print(-71.087133,6); Serial.print(",");
  }
  
  gps.stats(&chars, &sentences, &failed);
  
  // dummy variables
  //Serial.print(73.242342); Serial.print(","); Serial.print(46.19919); Serial.print(",");
//  if (chars == 0);
//    //Serial.println("** No characters received from GPS: check wiring **");
//  
}

void setup() {
  Serial.begin(4800);
  ss.begin(9600);
}

void loop() {
  
  // test the wind sensors
//  Serial.print("Wind 1: "); Serial.print(get_anem(1)); Serial.print("   ");
//  Serial.print("Wind 2: "); Serial.print(get_anem(2)); Serial.print("   ");
//  Serial.print("Wind 3: "); Serial.print(get_anem(3)); Serial.print("   ");
//  Serial.print("Wind 4: "); Serial.print(get_anem(4)); Serial.println("   ");
//  delay(500);
  
  // main code for Antenna Box loop
  Serial.print(get_heading(), 6); Serial.print(",");
  get_wind();
  get_gps(); Serial.print("\n");
  delay(100);


}