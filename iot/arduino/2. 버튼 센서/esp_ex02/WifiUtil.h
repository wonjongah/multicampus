#ifndef __WIFI_UTIL_H__
#define __WIFI_UTIL_H__
// pragma once

#include <SoftwareSerial.h>
#include <WiFiEsp.h>

class WifiUtil {
    private:
        const char * ssid; // 값 상수 읽기만 가능
        const char * password;
        SoftwareSerial softSerial;
        int status = WL_IDLE_STATUS; // Status
    public:
        WifiUtil(int rx, int tx);
        void init(const char * ssid,
        const char * password);
        void checkShield();
        void printInfo();
        int check(); // 접속
};

#endif