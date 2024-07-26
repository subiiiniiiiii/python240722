import sys
import can
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit

class UDSClient:
    def __init__(self, channel='vcan0', bustype='socketcan'):
        self.bus = can.interface.Bus(channel=channel, bustype=bustype)
        self.tx_id = 0x7DF  # UDS 요청 ID
        self.rx_id = 0x7E8  # UDS 응답 ID

    def send_command(self, command):
        message = can.Message(arbitration_id=self.tx_id, data=command, extended_id=False)
        self.bus.send(message)
        response = self.bus.recv(timeout=1.0)
        if response and response.arbitration_id == self.rx_id:
            return response.data
        else:
            return None

class UDSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.uds_client = UDSClient()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('UDS Diagnostic Tool')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.command_label = QLabel('UDS Command:')
        layout.addWidget(self.command_label)

        self.command_input = QLineEdit()
        layout.addWidget(self.command_input)

        self.send_button = QPushButton('Send Command')
        layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.send_command)

        self.response_label = QLabel('Response:')
        layout.addWidget(self.response_label)

        self.response_output = QTextEdit()
        self.response_output.setReadOnly(True)
        layout.addWidget(self.response_output)

    def send_command(self):
        command_text = self.command_input.text()
        command = [int(x, 16) for x in command_text.split()]
        response = self.uds_client.send_command(command)
        if response:
            response_text = ' '.join(format(x, '02X') for x in response)
        else:
            response_text = 'No response or timeout'
        self.response_output.append(f'Command: {command_text}\nResponse: {response_text}\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uds_app = UDSApp()
    uds_app.show()
    sys.exit(app.exec_())
