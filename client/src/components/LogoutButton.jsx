import React from "react";

function LogoutButton() {
  const handleLogout = () => {
    sessionStorage.removeItem("userToken");
    window.location.reload();
  };

  return (
    <button className='btn btn-primary' onClick={handleLogout}>
      Logout
    </button>
  );
}

export default LogoutButton;
