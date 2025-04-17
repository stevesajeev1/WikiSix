import { useState } from 'react';

import type { Result } from '../types';

import Header from './Header';
import Input from './Input';
import Graph from './Graph';
import Paths from './Paths';
import UserPaths from './UserPaths';

export default function App() {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const [result, setResult] = useState<Result | null>(null);

  const calculate = async () => {
    const payload = {
      "start": start.trim(),
      "end": end.trim()
    }

    const response = await fetch('/calculate', {
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      }
    });

    if (!response.ok) {
      setResult(null);
      const text = await response.text();
      alert(text);
    } else {
      const json = await response.json() as Result;
      setResult(json);
    }

    // Clear inputs
    setStart("");
    setEnd("");
  }

  return (
    <>
      <Header />
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
        <UserPaths user={result.user} />
      </>
      }
    </>
  )
}