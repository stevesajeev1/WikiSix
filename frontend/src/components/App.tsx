import "../styles/App.css";

import Header from './Header';
import Input from './Input';
import Graph from './Graph';
import Paths from './Paths';
import UserPaths from './UserPaths';

export default function App() {
  return (
    <>
      <Header />
      <Input />
      <Graph />
      <div id="paths">
        <Paths />
        <UserPaths />
      </div>
    </>
  )
}