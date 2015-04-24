#include <stdio.h>

#include <lcm/lcm-cpp.hpp>
#include "lilylcm/L06Depth.hpp"
#include "lilylcm/L07Humidity.hpp"
#include "lilylcm/L08Tempurature.hpp"
#include "lilylcm/L14LEDs.hpp"
#include "lilylcm/L16ChargerCommand.hpp"
#include "lilylcm/L19DockCommand.hpp"

class Handler 
{
    public:
        ~Handler() {}

        void handleMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const lilylcm* msg)
        {
            int i;
            printf("Received message on channel \"%s\":\n", chan.c_str());
            printf("  timestamp   = %lld\n", (long long)msg->timestamp);
            printf("  position    = (%f, %f, %f)\n",
                    msg->position[0], msg->position[1], msg->position[2]);
            printf("  orientation = (%f, %f, %f, %f)\n",
                    msg->orientation[0], msg->orientation[1], 
                    msg->orientation[2], msg->orientation[3]);
            printf("  ranges:");
            for(i = 0; i < msg->num_ranges; i++)
                printf(" %d", msg->ranges[i]);
            printf("\n");
            printf("  name        = '%s'\n", msg->name.c_str());
            printf("  enabled     = %d\n", msg->enabled);
        }
};

int main(int argc, char** argv)
{
    lcm::LCM lcm;

    if(!lcm.good())
        return 1;

    Handler handlerObject;
    lcm.subscribe("POD_Depth", &Handler::handleMessage, &handlerObject);
    lcm.subscribe("POD_Humidity", &Handler::handleMessage, &handlerObject);
    lcm.subscribe("POD_Tempurature", &Handler::handleMessage, &handlerObject);
    lcm.subscribe("POD_LED", &Handler::handleMessage, &handlerObject);
    lcm.subscribe("POD_Charge", &Handler::handleMessage, &handlerObject);
    lcm.subscribe("POD_Magnet", &Handler::handleMessage, &handlerObject);

    while(0 == lcm.handle());

    return 0;
}

