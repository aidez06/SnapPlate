QML = """
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Window {
    width: 1200
    height: 900
    visible: true
    title: "SnapPlate"
    color: "black" // Set the background color to black

    Rectangle {
        width: 840
        height: 100
        color: Qt.rgba(1, 1, 1, 0.06) // Set the color to white with 6% opacity
        radius: 50 // Set the corner radius to create a curved rectangle
        anchors.top: parent.top // Anchor the top of the rectangle to the top of its parent
        anchors.horizontalCenter: parent.horizontalCenter // Center horizontally in relation to parent's center
        anchors.topMargin: parent.height * 0.1 // Set the top margin to 10% of the parent's height

        Button {
            width: 200
            height: 40
            text: "Launch App"
            background: Rectangle {
                color: "transparent"
                border.color: "#21be2b"
                radius: 20
            }
            contentItem: Text {
                text: parent.text // Display the button text
                font.pixelSize: 16 // Font size
                color: "#2D8C1D" // Text color
                verticalAlignment: Text.AlignVCenter // Align text vertically
                horizontalAlignment: Text.AlignHCenter // Align text horizontally
            }
        anchors.horizontalCenter: parent.horizontalCenter // Center horizontally in relation to parent's center
        anchors.verticalCenter: parent.verticalCenter // Center vertical in relation to parent's center
        } 
    }
}

"""