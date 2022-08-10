import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { ApiService } from "./Services";

import App from "./App";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

ApiService.init("https://api.twitter.com/2");
ApiService.setHeader();

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
