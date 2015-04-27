void transmitData(float windDir, float windMag, float compassHeading, float gpsLong, float gpsLat):
    String result = "";
    String separator = ",";
    result +=  String(winDir) + separator;
    result += String(winMag) + separator;
    result += String(compassHeading) + separator;
    result += String(gpsLong) + separator;
    result += String(gpsLat) + separator;
    serial.println(result);
    
