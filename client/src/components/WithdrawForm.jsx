import React, { useState } from "react";
import { NumericFormat } from "react-number-format";

function WithdrawForm({ accountID, setCount, setShowModal }) {
  const [formValue, setFormValue] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    let value = parseFloat(formValue) * 100;
    const response = await fetch(
      `http://127.0.0.1:5000/accounts/${accountID}/withdraw`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: sessionStorage.getItem("userToken"),
        },
        body: JSON.stringify({
          value,
        }),
      }
    );
    await response.json();
    if (response.ok) {
      setCount((count) => count + 1);
      setShowModal(false);
      alert("Saque realizado com sucesso");
    } else {
      alert("Falha ao realizar saque");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className='mb-3'>
        <label htmlFor='balance' className='form-label'>
          Valor do Saque
        </label>
        <NumericFormat
          value={formValue}
          onValueChange={(values) => setFormValue(values.value)}
          thousandSeparator={true}
          decimalScale={2}
          fixedDecimalScale={true}
          prefix={"$"}
          className='form-control'
          id='balance'
        />
      </div>

      <button type='submit' className='btn btn-primary'>
        Sacar
      </button>
    </form>
  );
}

export default WithdrawForm;
