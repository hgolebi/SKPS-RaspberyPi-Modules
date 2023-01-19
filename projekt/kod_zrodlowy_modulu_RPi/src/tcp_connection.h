#ifndef TCP_CONNECTION
#define TCP_CONNECTION

#include <netinet/in.h>
#include <sys/socket.h>


class TCP_Connection
{
    private:
        int server_fd, new_socket;
        struct sockaddr_in address;
        int opt = 1;
        int addrlen = sizeof(address);
        int port;
    public:
        TCP_Connection(int port);
        void set_connection();
        void send_data(float data);
        void close_connection();
};

#endif