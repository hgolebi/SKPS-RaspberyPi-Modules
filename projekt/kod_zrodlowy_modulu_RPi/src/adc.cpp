#include "i2c.h"
#include "tcp_connection.h"
#include <iostream>
#include <unistd.h>


using namespace std;

int main(int argc, char const* argv[])
{
    TCP_Connection tcp = TCP_Connection(8080);
    tcp.set_connection();
    cout<<"Connection set"<<endl;
    I2CConnector connector = I2CConnector();
    connector.init();
    cout<<"i2c connection established"<<endl;
    while(true){
        int data = connector.readData(2);
        float result = data * 0.001; 
        cout<<result<<endl;
        tcp.send_data(result);
        usleep(300000);
    }
    tcp.close_connection();
}