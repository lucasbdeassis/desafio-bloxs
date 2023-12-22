import AccountsTable from "../components/AccountsTable";
import TransactionsTable from "../components/TransactionsTable";
import UserBalance from "../components/UserBalance";
import LogoutButton from "../components/LogoutButton";
import { useState } from "react";

function DashboarView() {
  const [count, setCount] = useState(0);
  return (
    <div className='container'>
      <div className='row mt-3 justify-content-center'>
        <div className='col-3'>
          <LogoutButton />
        </div>
      </div>
      <div className='row mt-5' style={{ maxWidth: "250px" }}>
        <UserBalance />
      </div>
      <div className='row mt-5'>
        <AccountsTable count={count} setCount={setCount} />
      </div>
      <div className='row mt-5'>
        <TransactionsTable count={count} setCount={setCount} />
      </div>
    </div>
  );
}

export default DashboarView;
