import React, { useState, useEffect } from "react";
import CreateAccountForm from "./CreateAccountForm";

function AccountsTable() {
  const [accounts, setAccounts] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [count, setCount] = useState(0);
  const [maxAccounts, setMaxAccounts] = useState(10);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/accounts", {
      headers: {
        Authorization: sessionStorage.getItem("userToken"),
      },
    })
      .then((response) => response.json())
      .then((data) => setAccounts(data))
      .catch((error) => console.error("Error:", error));
  }, [count]);

  return (
    <div className='container'>
      <div className='card'>
        <div className='card-header d-flex justify-content-between'>
          <div>Contas</div>
          <button
            className='btn btn-primary'
            onClick={() => setShowModal(true)}
          >
            +
          </button>
        </div>
        <div class='card-body'>
          <table className='table'>
            <thead>
              <tr>
                <th scope='col'>#</th>
                <th scope='col'>Nome</th>
                <th scope='col'>Saldo</th>
                <th scope='col'>Situação</th>
              </tr>
            </thead>
            <tbody>
              {accounts.slice(0, maxAccounts).map((account, index) => (
                <tr key={index}>
                  <th scope='row'>{index + 1}</th>
                  <td>{account.name}</td>
                  <td>${(account.balance / 100).toFixed(2)}</td>
                  <td>{account.is_active ? "Ativa" : "Bloqueada"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className='card-footer text-center'>
          <a
            className='button'
            onClick={() => setMaxAccounts((maxAccounts) => maxAccounts + 5)}
          >
            mostrar mais
          </a>
          <span> | </span>
          <a
            className='button'
            onClick={() => setMaxAccounts((maxAccounts) => maxAccounts - 5)}
          >
            mostrar menos
          </a>
        </div>
      </div>
      {showModal && (
        <div className='modal fade show d-block' tabIndex='-1'>
          <div className='modal-dialog modal-dialog-centered'>
            <div className='modal-content'>
              <div className='modal-header'>
                <h5 className='modal-title'>Nova Conta</h5>
                <button
                  type='button'
                  className='btn-close'
                  onClick={() => setShowModal(false)}
                ></button>
              </div>
              <div className='modal-body'>
                <CreateAccountForm
                  setCount={setCount}
                  setShowModal={setShowModal}
                />
              </div>
              <div className='modal-footer'>
                <button
                  type='button'
                  className='btn btn-secondary'
                  onClick={() => setShowModal(false)}
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default AccountsTable;
