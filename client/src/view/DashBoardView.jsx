import AccountsTable from "../components/AccountsTable";
import TransactionsTable from "../components/TransactionsTable";
import UserBalance from "../components/UserBalance";

function DashboarView() {
  return (
    <div className='container'>
      <div className='row mt-5'>
        <UserBalance />
      </div>
      <div className='row mt-5'>
        <AccountsTable />
      </div>
      <div className='row mt-5'>
        <TransactionsTable />
      </div>
    </div>
  );
}

export default DashboarView;
