class ScreenManager {
    Document;
    alertContent;

    constructor(Document = null) {
      this.Document = Document ?? document.getElementsByTagName("body")[0];

      this.alertContent = document.createElement("div");
      this.alertContent.id = "alert";

      //     this.alertContent.innerHTML = `

      //     <div class="alertLine ">normal</div>

      // <div class="alertLine danger">danger</div>
      // <div class="alertLine success">success</div>
      // <div class="alertLine warning">warning</div>
      //     `;

      this.Document.appendChild(this.alertContent);
    }

    alert(message, type = "") {
      const alert = document.createElement("div");
      alert.classList = "micro alertLine " + type;
      alert.innerHTML = message;

      this.alertContent.appendChild(alert);

      setTimeout(() => {
        alert.classList.remove("micro");
        setTimeout(() => {
          alert.classList.add("micro");
          setTimeout(() => {
            this.alertContent.removeChild(alert);
          }, 1000);
        }, 5000);
      }, 100);
    }
  }