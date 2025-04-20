import "../styles/App.css";

import { useState } from 'react';

import type { Result } from '../types';

import Header from './Header';
import Input from './Input';
import Graph from './Graph';
import Paths from './Paths';
import UserPath from './UserPath';
import Footer from './Footer';

export default function App() {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const [result, setResult] = useState<Result | null>(null);

  const calculate = async () => {
    const payload = {
      "start": start.trim(),
      "end": end.trim()
    }

    const response = await fetch('/api/calculate', {
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      }
    });

    if (!response.ok) {
      setResult(null);
      const text = await response.text();
      setStart("");
      setEnd("");
      alert(text);
    } else {
      const json = await response.json() as Result;
      setResult(json);
    }
  }

  return (
    <>
      <Header />
      <div id="content">
        <Input
          start={start}
          setStart={setStart}
          end={end}
          setEnd={setEnd}
          calculate={calculate}
        />
        {result !== null &&
        <>
          <Graph result={result} />
          <Paths paths={result.paths} />
          <UserPath user={result.user} />
        </>
        }
      </div>
      <Footer />
    </>
  )
}