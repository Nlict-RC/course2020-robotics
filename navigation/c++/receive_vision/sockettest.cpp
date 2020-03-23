#include "sockettest.h"
#include "vision_detection.pb.h"
namespace{
    int port = 23333;
}

sockettest::sockettest(QObject *parent) : QObject(parent),socket(nullptr)
{
    socket = new QUdpSocket();
    socket->bind(QHostAddress::AnyIPv4, port, QUdpSocket::ShareAddress);
    connect(socket,SIGNAL(readyRead()),this,SLOT(handle()),Qt::DirectConnection);
    qDebug() << "markdebug : constructor" ;
}
void sockettest::handle(){
    static QByteArray data;
    static Vision_DetectionFrame vision;
    while(socket->hasPendingDatagrams()){
        data.resize(socket->pendingDatagramSize());
        socket->readDatagram(data.data(),data.size());
        vision.ParseFromArray(data,data.size());
        auto ball = vision.balls();
//        qDebug() << ball.x() << ball.y() << ball.vel_x() << ball.vel_y();
        int blue_size = vision.robots_blue_size();
        for(int i=0;i<blue_size;i++){
            auto blue = vision.robots_blue(i);
            if(blue.robot_id() == 0)
                qDebug() << blue.robot_id() << blue.x() << blue.y();
        }
//        qDebug() << "markdebug : " << data.toHex();
    }
}
