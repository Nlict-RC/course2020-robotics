#ifndef SOCKETTEST_H
#define SOCKETTEST_H

#include <QObject>
#include <QUdpSocket>
class sockettest : public QObject
{
    Q_OBJECT
public:
    explicit sockettest(QObject *parent = nullptr);
public slots:
    void handle();
public:
    QUdpSocket * socket;
};

#endif // SOCKETTEST_H
