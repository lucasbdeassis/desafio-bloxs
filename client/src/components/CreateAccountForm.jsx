import React, { useState } from "react";
import { NumericFormat } from "react-number-format";

function CreateAccountForm({ setCount, setShowModal }) {
  const [name, setName] = useState("");
  const [formBalance, setFormBalance] = useState("");
  const [formMaxDailyWithdraw, setFormMaxDailyWithdraw] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    let balance = parseFloat(formBalance) * 100;
    let maxDailyWithdraw = parseFloat(formMaxDailyWithdraw) * 100;
    const response = await fetch("http://127.0.0.1:5000/accounts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: sessionStorage.getItem("userToken"),
      },
      body: JSON.stringify({
        name,
        balance,
        max_daily_withdraw: maxDailyWithdraw,
      }),
    });
    await response.json();
    if (response.ok) {
      setCount((count) => count + 1);
      setShowModal(false);
      alert("Account created successfully");
    } else {
      alert("Failed to create account");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className='mb-3'>
        <label htmlFor='name' className='form-label'>
          Nome
        </label>
        <input
          type='text'
          className='form-control'
          id='name'
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </div>
      <div className='mb-3'>
        <label htmlFor='balance' className='form-label'>
          Saldo Inicial
        </label>
        <NumericFormat
          value={formBalance}
          onValueChange={(values) => setFormBalance(values.value)}
          thousandSeparator={true}
          decimalScale={2}
          fixedDecimalScale={true}
          prefix={"$"}
          className='form-control'
          id='balance'
        />
      </div>
      <div className='mb-3'>
        <label htmlFor='maxDailyWithdraw' className='form-label'>
          Saque Máximo Diário
        </label>
        <NumericFormat
          value={formMaxDailyWithdraw}
          onValueChange={(values) => setFormMaxDailyWithdraw(values.value)}
          thousandSeparator={true}
          decimalScale={2}
          fixedDecimalScale={true}
          prefix={"$"}
          className='form-control'
          id='maxDailyWithdraw'
        />
      </div>
      <button type='submit' className='btn btn-primary'>
        Criar
      </button>
    </form>
  );
}

export default CreateAccountForm;
