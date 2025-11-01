// overrides/plugins/load-custom-css/index.js

const plugin = {
  id: "load-custom-css:plugin",
  autoStart: true,
  activate: () => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = "./files/custom.css";  // Pfad relativ zur Lite-Distribution
    document.head.appendChild(link);
    console.log("Custom CSS loaded from files/custom.css");
  }
};

export default plugin;
