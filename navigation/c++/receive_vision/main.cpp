#include <QCoreApplication>
#include <sockettest.h>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    sockettest test;
    return a.exec();
}
