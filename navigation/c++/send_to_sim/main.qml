import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import Client 1.0 as Client
Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")
    Client.Sender{
        id : sender;
    }
    Button{
        text : "Button";
        onClicked: {
            sender.send();
        }
    }
}
