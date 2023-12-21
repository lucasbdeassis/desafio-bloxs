import React, { useState, useEffect } from "react";

function AccountsTable() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/accounts", {
      headers: {
        Authorization: sessionStorage.getItem("userToken"),
      },
    })
      .then((response) => response.json())
      .then((data) => setAccounts(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <table className='table'>
      <thead>
        <tr>
          <th scope='col'>#</th>
          <th scope='col'>Balance</th>
          <th scope='col'>Is Active</th>
        </tr>
      </thead>
      <tbody>
        {accounts.map((account, index) => (
          <tr key={index}>
            <th scope='row'>{index + 1}</th>
            <td>${account.balance}</td>
            <td>{account.is_active ? "Yes" : "No"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default AccountsTable;
