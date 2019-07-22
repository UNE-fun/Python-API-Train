from flask import jsonify, Flask

#controllerをインポートしたいのでこのパッケージを使用する
import controller

app = Flask(__name__)

class PCI(controller.PingControllerInterface):
    def pong(self):
        print("Called pci.pong")

@app.route("/ping", methods=["GET"])
def apiget():
    #これだと500エラーになってしまう
    #return controller.ping_controller.PingController.pong()
    #まずはping_controllerクラスを作る
    pci = PCI()
    pingcontroller = controller.PingController(pci)
    return pingcontroller.pong()

if __name__ == "__main__":
    app.debug = True
    app.run()
