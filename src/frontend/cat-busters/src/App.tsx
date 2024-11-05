import { FormProvider, useForm } from "react-hook-form";
import "./App.css";
import { StyledDiv, StyledInput } from "./App.styles";
import { Button } from "./components/ui/button";
import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
} from "./components/ui/form";
import Logo from "./assets/logo.png";
import { useNavigate } from "react-router-dom";

function App() {
  const navigate = useNavigate();

  const form = useForm({
    defaultValues: {
      username: "",
      password: "",
    },
  });

  return (
    <StyledDiv className="flex flex-col gap-3 ml-[25%]  mt-[10%]">
      <img src={Logo} />
      <FormProvider {...form}>
        <form
          onSubmit={form.handleSubmit(() => {})}
          className="flex flex-col space-y-6 gap-3 w-full"
        >
          <div className="flex flex-col w-full space-y-6 gap-3">
            <FormField
              control={form.control}
              name="username"
              render={({ field }) => (
                <FormItem className="grid w-full items-center gap-1.5">
                  <div>
                    <FormLabel htmlFor="username">Nome</FormLabel>
                  </div>
                  <FormControl>
                    <StyledInput placeholder="Username" {...field} />
                  </FormControl>
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="password"
              render={({ field }) => (
                <FormItem className="grid w-full items-center gap-1.5">
                  <div className="flex">
                    <FormLabel htmlFor="password">Senha</FormLabel>
                  </div>
                  <FormControl>
                    <StyledInput
                      type="password"
                      id="password"
                      placeholder="Senha"
                      {...field}
                    />
                  </FormControl>
                </FormItem>
              )}
            />
            <Button
              onClick={() => navigate("/upload")}
              className="mt-2 w-full"
              type="submit"
            >
              Entrar
            </Button>
          </div>
        </form>
      </FormProvider>
    </StyledDiv>
  );
}

export default App;
