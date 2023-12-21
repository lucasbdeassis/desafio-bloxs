import React, { useState, useEffect } from "react";

function TransactionsTable() {
  const [transactions, setTransactions] = useState([]);
  const [maxTransactions, setMaxTransactions] = useState(10);

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
    <div className='container'>
      <div className='card'>
        <div className='card-header'>Últimas Transações</div>
        <div class='card-body'>
          <table className='table'>
            <thead>
              <tr>
                <th scope='col'>#</th>
                <th scope='col'>Amount</th>
                <th scope='col'>Transaction Date</th>
              </tr>
            </thead>
            <tbody>
              {transactions
                .sort(
                  (a, b) =>
                    new Date(b.transaction_date) - new Date(a.transaction_date)
                )
                .slice(0, maxTransactions)
                .map((transaction, index) => (
                  <tr key={index}>
                    <th scope='row'>{index + 1}</th>
                    <td>${(transaction.amount / 100).toFixed(2)}</td>
                    <td>
                      {new Date(
                        transaction.transaction_date
                      ).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
        <div className='card-footer text-center'>
          <a
            className='button'
            onClick={() =>
              setMaxTransactions((maxTransactions) => maxTransactions + 5)
            }
          >
            mostrar mais
          </a>
          <span> | </span>
          <a
            className='button'
            onClick={() =>
              setMaxTransactions((maxTransactions) => maxTransactions - 5)
            }
          >
            mostrar menos
          </a>
        </div>
      </div>
    </div>
  );
}

export default TransactionsTable;
