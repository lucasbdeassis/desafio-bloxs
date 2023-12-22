import React, { useState, useEffect } from "react";
import CreateAccountForm from "./CreateAccountForm";
import DepositForm from "./DepositForm";
import WithdrawForm from "./WithdrawForm";

function AccountsTable({ count, setCount }) {
  const [accounts, setAccounts] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [maxAccounts, setMaxAccounts] = useState(10);
  const [showDepositModal, setShowDepositModal] = useState(false);
  const [showWithdrawModal, setShowWithdrawModal] = useState(false);
  const [accountID, setAccountID] = useState("");

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

  const handleBlock = async (accountID, isActive) => {
    let command = isActive ? "block" : "unblock";
    const response = await fetch(
      `http://127.0.0.1:5000/accounts/${accountID}/${command}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: sessionStorage.getItem("userToken"),
        },
      }
    );
    await response.json();
    if (response.ok) {
      setCount((count) => count + 1);
      setShowModal(false);
      alert(
        isActive
          ? "Conta bloqueada com sucesso"
          : "Conta desbloqueada com sucesso"
      );
    } else {
      alert("Erro");
    }
  };

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
                <th scope='col'></th>
              </tr>
            </thead>
            <tbody>
              {accounts.slice(0, maxAccounts).map((account, index) => (
                <tr key={index}>
                  <th scope='row'>{index + 1}</th>
                  <td>{account.name}</td>
                  <td>${(account.balance / 100).toFixed(2)}</td>
                  <td>{account.is_active ? "Ativa" : "Bloqueada"}</td>
                  <td>
                    <button
                      className='btn btn-success'
                      onClick={() => {
                        setShowDepositModal(true);
                        setAccountID(account.id);
                      }}
                    >
                      Depositar
                    </button>
                    <span> </span>
                    <button
                      className='btn btn-warning'
                      onClick={() => {
                        setShowWithdrawModal(true);
                        setAccountID(account.id);
                      }}
                    >
                      Sacar
                    </button>
                    <span> </span>
                    <button
                      className={
                        account.is_active ? "btn btn-danger" : "btn btn-primary"
                      }
                      onClick={() => {
                        handleBlock(account.id, account.is_active);
                        setAccountID(account.id);
                      }}
                    >
                      {account.is_active ? "Bloquear" : "Desbloquear"}
                    </button>
                  </td>
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
      {showDepositModal && (
        <div className='modal fade show d-block' tabIndex='-1'>
          <div className='modal-dialog modal-dialog-centered'>
            <div className='modal-content'>
              <div className='modal-header'>
                <h5 className='modal-title'>Deposito</h5>
                <button
                  type='button'
                  className='btn-close'
                  onClick={() => setShowDepositModal(false)}
                ></button>
              </div>
              <div className='modal-body'>
                <DepositForm
                  accountID={accountID}
                  setCount={setCount}
                  setShowModal={setShowDepositModal}
                />
              </div>
              <div className='modal-footer'>
                <button
                  type='button'
                  className='btn btn-secondary'
                  onClick={() => setShowDepositModal(false)}
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
      {showWithdrawModal && (
        <div className='modal fade show d-block' tabIndex='-1'>
          <div className='modal-dialog modal-dialog-centered'>
            <div className='modal-content'>
              <div className='modal-header'>
                <h5 className='modal-title'>Saque</h5>
                <button
                  type='button'
                  className='btn-close'
                  onClick={() => setShowWithdrawModal(false)}
                ></button>
              </div>
              <div className='modal-body'>
                <WithdrawForm
                  accountID={accountID}
                  setCount={setCount}
                  setShowModal={setShowWithdrawModal}
                />
              </div>
              <div className='modal-footer'>
                <button
                  type='button'
                  className='btn btn-secondary'
                  onClick={() => setShowWithdrawModal(false)}
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
