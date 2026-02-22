import os
from interfaces.gradio_ui import GradioUI

if __name__ == "__main__":
    app = GradioUI()
    port = int(os.environ.get("PORT", 8080))
    print("ENVIRON: ", os.environ)
    app.ui.launch(
        server_name="0.0.0.0",
        server_port=port,
        allowed_paths=["/tmp"]
    )





