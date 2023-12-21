import LoginView from "./view/LoginView";
import DashboarView from "./view/DashBoardView";

import { useEffect, useState } from "react";

function App() {
  // const [userToken, setUserToken] = useState(
  //   sessionStorage.getItem("userToken")
  // );

  const userToken = sessionStorage.getItem("userToken");

  useEffect(() => {
    const verifyUserToken = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/auth/validate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ token: userToken }),
        });

        if (response.status !== 200) {
          sessionStorage.removeItem("userToken");
        }
      } catch (error) {
        console.error(error);
      }
    };

    if (
      userToken &&
      typeof userToken === "string" &&
      userToken.trim() !== "" &&
      userToken !== "undefined"
    ) {
      verifyUserToken();
    }
  }, [userToken]);

  if (
    userToken &&
    typeof userToken === "string" &&
    userToken.trim() !== "" &&
    userToken !== "undefined"
  ) {
    return (
      <>
        <DashboarView />
      </>
    );
  }

  return (
    <>
      <LoginView />
    </>
  );
}

export default App;
