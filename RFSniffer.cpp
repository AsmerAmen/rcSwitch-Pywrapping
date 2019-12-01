
#include "RCSwitch.h"
     
RCSwitch mySwitch;
 
extern "C" unsigned long getValue(){
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