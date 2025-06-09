const WebSocket = require("ws");
const { spawn } = require("child_process");

const wss = new WebSocket.Server({ port: 3002 });

wss.on("connection", function connection(ws) {
  console.log("Client connected");

  ws.on("message", function incoming(message) {
    console.log("Received:", message.toString());

    const py = spawn("python", ["../rag_engine/answer.py", message.toString()]);

    py.stdout.on("data", (data) => {
      ws.send(data.toString());
    });
  });
});
