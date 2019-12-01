
#include "RCSwitch.h"
#define PIN 2
//RCSwitch mySwitch;

 
extern "C"{
    void init(){
        myRC.enableReceive(PIN);
    }


    unsigned long getValue(){
        unsigned long value = 0UL;
        if (myRC.available()) {
            value = myRC.getReceivedValue();
            /*
            if (value == 0UL) {
              printf("Unknown encoding\n");
            } else {
              printf("Received %lu\n", mySwitch.getReceivedValue() );
            }
            fflush(stdout);
            */

            myRC.resetAvailable();
        }
        return value;
    }
}