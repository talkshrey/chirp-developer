import * as React from "react";
import { TextField, Button } from "@mui/material";
import Stack from "@mui/material/Stack";
import ApiService from "../Services/Api";
import { backendRoutes } from "../Routes/Routes";

export default function Search() {
  const [input, setInput] = React.useState();

  function handleChange(e) {
    console.log(e.target.value);
    setInput(e.target.value);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    console.log(input);
    const [res, err] = await ApiService.get(
      backendRoutes.search(`%23${input}`)
    );
    if (res) {
      console.log(res);
    } else {
      console.log(err);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <Stack spacing={2} sx={{ width: 300 }}>
        <TextField
          onChange={handleChange}
          id="outlined-basic"
          label="Search input"
        />
        <Button variant="contained" type="submit">
          Search
        </Button>
      </Stack>
    </form>
  );
}
