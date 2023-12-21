import React, { useState, useEffect } from "react";

function TransactionsTable() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/transactions", {
      headers: {
        Authorization: sessionStorage.getItem("userToken"),
      },
    })
      .then((response) => response.json())
      .then((data) => setTransactions(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <table className='table'>
      <thead>
        <tr>
          <th scope='col'>#</th>
          <th scope='col'>Amount</th>
          <th scope='col'>Transaction Date</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((transaction, index) => (
          <tr key={index}>
            <th scope='row'>{index + 1}</th>
            <td>${transaction.amount}</td>
            <td>
              {new Date(transaction.transaction_date).toLocaleDateString()}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TransactionsTable;
