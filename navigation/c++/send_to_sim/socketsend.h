#ifndef SOCKETSEND_H
#define SOCKETSEND_H

#include <QObject>

class socketsend : public QObject
{
    Q_OBJECT
public:
    explicit socketsend(QObject *parent = nullptr);
    Q_INVOKABLE void send();

signals:

public slots:
};

#endif // SOCKETSEND_H
