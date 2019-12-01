
#include "RCSwitch.h"
#define PIN 2
RCSwitch mySwitch;

 
extern "C"{
    void init(){
        mySwitch.enableReceive(PIN);
    }

    
    unsigned long getValue(){
        unsigned long value = 0UL;
        if (mySwitch.available()) {
            value = mySwitch.getReceivedValue();
            /*
            if (value == 0UL) {
              printf("Unknown encoding\n");
            } else {
              printf("Received %lu\n", mySwitch.getReceivedValue() );
            }
            fflush(stdout);
            */

            mySwitch.resetAvailable();
        }
        return value;
    }
}