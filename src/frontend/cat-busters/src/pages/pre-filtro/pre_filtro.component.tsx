import { Button } from "@/components/ui/button";
import Logo from "../../assets/logo.png";
import { Checkbox } from "@radix-ui/themes";
import { addDays, format } from "date-fns";
import React from "react";
import { DateRange } from "react-day-picker";
import { Calendar } from "@/components/ui/calendar";
import { CalendarIcon } from "@radix-ui/react-icons";
import { cn } from "@/lib/utils";
import { useNavigate } from "react-router-dom";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

export function Prefiltro() {
  const navigate = useNavigate();
  const [date, setDate] = React.useState<DateRange | undefined>({
    from: new Date(2022, 0, 20),
    to: addDays(new Date(2022, 0, 20), 20),
  });

  return (
    <div className="flex w-full flex-col h-[100vh]">
      <img className="w-[125px] " src={Logo} />
      <div className="flex flex-col w-full justify-top items-start pl-20 pr-20">
        <div className="flex flex-col w-full justify-top gap-4 pt-[94px] items-start">
          <label
            className="text-2xl font-bold"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            Ótimo! Agora caso queira fazer um pré filtro antes da visualização
            selecione as features que são do seu interesse. Após sua escolha
            clique em “Visualizar”.
          </label>

          <label
            className="text-center text-xl"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            1. Quais tipos de matrícula?
          </label>

          <div className="flex items-center space-x-2">
            <Checkbox
              id="terms2"
              className="w-[30px] h-[30px] text-[#072C59] border-[#072C59]"
            />
            <label
              htmlFor="terms2"
              className="font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              style={{ fontSize: "15px", color: "#072C59" }}
            >
              Comercial
            </label>
          </div>
          <div className="flex items-center space-x-2">
            <Checkbox
              id="terms2"
              className="w-[30px] h-[30px] text-[#072C59] border-[#072C59]"
            />
            <label
              htmlFor="terms2"
              className="font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              style={{ fontSize: "15px", color: "#072C59" }}
            >
              Industrial
            </label>
          </div>
          <div className="flex items-center space-x-2">
            <Checkbox
              id="terms2"
              className="w-[30px] h-[30px] text-[#072C59] border-[#072C59]"
            />
            <label
              htmlFor="terms2"
              className="font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              style={{ fontSize: "15px", color: "#072C59" }}
            >
              Residencial
            </label>
          </div>
          <div className="flex items-center space-x-2">
            <Checkbox
              id="terms2"
              className="w-[30px] h-[30px] text-[#072C59] border-[#072C59]"
            />
            <label
              htmlFor="terms2"
              className="font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              style={{ fontSize: "15px", color: "#072C59" }}
            >
              Pública
            </label>
          </div>
          <div className="flex items-center space-x-2">
            <Checkbox
              id="terms2"
              className="w-[30px] h-[30px] text-[#072C59] border-[#072C59]"
            />
            <label
              htmlFor="terms2"
              className="font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
              style={{ fontSize: "15px", color: "#072C59" }}
            >
              Todos
            </label>
          </div>

          <label
            className="text-center text-xl"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            2. Qual o intervalo de tempo?
          </label>
          <div>
            <Popover>
              <PopoverTrigger asChild>
                <Button
                  id="date"
                  variant={"outline"}
                  className={cn(
                    "w-[300px] justify-start text-left font-normal",
                    !date && "text-muted-foreground"
                  )}
                >
                  <CalendarIcon className="mr-2 h-4 w-4" />
                  {date?.from ? (
                    date.to ? (
                      <>
                        {format(date.from, "LLL dd, y")} -{" "}
                        {format(date.to, "LLL dd, y")}
                      </>
                    ) : (
                      format(date.from, "LLL dd, y")
                    )
                  ) : (
                    <span>Pick a date</span>
                  )}
                </Button>
              </PopoverTrigger>
              <PopoverContent className="w-auto p-0" align="start">
                <Calendar
                  initialFocus
                  mode="range"
                  defaultMonth={date?.from}
                  selected={date}
                  onSelect={setDate}
                  numberOfMonths={2}
                />
              </PopoverContent>
            </Popover>
          </div>
          <label
            className="text-center text-xl"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            3. Qual o intervalo Mín-Max de consumo?
          </label>

          <Select>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Selecione o intervalo" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectLabel>Selecione o intervalo</SelectLabel>
                <SelectItem value="A - B">A - B</SelectItem>
                <SelectItem value="B - C">B - C</SelectItem>
                <SelectItem value="C - D">C - D</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <div className=" w-full flex justify-center">
            <Button
              onClick={() => navigate("/resultado")}
              className=" w-[30rem]"
            >
              Calcular
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
