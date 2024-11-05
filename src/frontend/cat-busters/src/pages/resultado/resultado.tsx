import { Button } from "@/components/ui/button";
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";
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
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Checkbox } from "@radix-ui/themes";
import { addDays } from "date-fns";
import React from "react";
import { DateRange } from "react-day-picker";
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts";
import Logo from "../../assets/logo.png";

const chartData = [
  { Categoria: "Comercial", Fraude: 186 },
  { Categoria: "Industrial", Fraude: 305 },
  { Categoria: "Pública", Fraude: 237 },
  { Categoria: "Residencial", Fraude: 73 },
];

const chartConfig = {
  Fraude: {
    label: "Fraude",
    color: "#2563eb",
  },
} satisfies ChartConfig;

const Categorias = [
  {
    Categoria: "Comercial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Pública",
    Medconsumo: "0,116",
    Probabilidade: "90%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Comercial",
    Medconsumo: "1",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Pública",
    Medconsumo: "0,116",
    Probabilidade: "90%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Comercial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Pública",
    Medconsumo: "0,116",
    Probabilidade: "90%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Comercial",
    Medconsumo: "1",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Comercial",
    Medconsumo: "1",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Industrial",
    Medconsumo: "0,116",
    Probabilidade: "10%",
    Resultado: "-",
  },
  {
    Categoria: "Pública",
    Medconsumo: "0,116",
    Probabilidade: "90%",
    Resultado: "Fraude",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "20%",
    Resultado: "-",
  },
  {
    Categoria: "Residencial",
    Medconsumo: "0,8",
    Probabilidade: "75%",
    Resultado: "Fraude",
  },
];

export function Resultado() {
  const [date, setDate] = React.useState<DateRange | undefined>({
    from: new Date(2022, 0, 20),
    to: addDays(new Date(2022, 0, 20), 20),
  });

  // Função para converter a string de porcentagem para número
  const parsePercentage = (percentage: string) => {
    return parseFloat(percentage.replace("%", ""));
  };

  return (
    <div className="flex w-full flex-col h-[100vh]">
      <img className="w-[125px] " src={Logo} />
      <div className="flex flex-row w-full justify-top items-start pl-20 pr-20 gap-[8px]">
        <div className="flex flex-col w-full justify-top gap-4 pt-[94px] items-start w-[45%]">
          <label
            className="text-2xl font-bold"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            Filtros
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
            2. Qual o intervalo Mín-Max de consumo?
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

          <div className=" w-full flex justify-start">
            <Button className=" w-[30rem] content-center">Filtrar</Button>
          </div>

          <label
            className="text-2xl font-bold"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            Insights
          </label>

          <div className="flex flex-row w-full justify-top items-start p-[8px] gap-[8px]">
            <div
              className="flex flex-col w-full justify-top gap-[8px] pt-[14,5px] items-center"
              style={{
                borderRadius: "8px",
                backgroundColor: "#C9D1DB",
                width: "inherit",
                padding: "8px",
              }}
            >
              <label
                className="font-normal text-nowrap"
                htmlFor="picture"
                style={{ color: "#072C59", width: "auto", fontSize: "large" }}
              >
                São possíveis fraudes
              </label>
              <label
                className="size-[40px] font-bold text-nowrap"
                htmlFor="picture"
                style={{ color: "#072C59", width: "auto", fontSize: "larger" }}
              >
                24%
              </label>
            </div>
            <div
              className="flex flex-col w-full justify-top gap-[8px] pt-[14,5px] items-center"
              style={{
                borderRadius: "8px",
                backgroundColor: "#C9D1DB",
                width: "inherit",
                padding: "8px",
              }}
            >
              <label
                className="font-normal text-nowrap"
                htmlFor="picture"
                style={{ color: "#072C59", width: "auto", fontSize: "large" }}
              >
                Média consumo fraudes
              </label>
              <label
                className="size-[40px] font-bold text-nowrap"
                htmlFor="picture"
                style={{ color: "#072C59", width: "auto", fontSize: "larger" }}
              >
                24%
              </label>
            </div>
          </div>

          <div
            className="flex flex-col w-full justify-top gap-[8px] pt-[14,5px] items-center"
            style={{
              borderRadius: "8px",
              backgroundColor: "#C9D1DB",
              padding: "8px",
            }}
          >
            <label
              className="font-normal text-nowrap"
              htmlFor="picture"
              style={{ color: "#072C59", width: "auto", fontSize: "large" }}
            >
              Probabilidade de fraudes por categoria
            </label>

            <ChartContainer
              config={chartConfig}
              className="min-h-[200px] w-full"
            >
              <BarChart accessibilityLayer data={chartData}>
                <CartesianGrid vertical={false} />
                <XAxis
                  dataKey="Categoria"
                  tickLine={false}
                  tickMargin={10}
                  axisLine={false}
                  tickFormatter={(value) => value.slice(0, 3)}
                />
                <ChartTooltip content={<ChartTooltipContent />} />
                <Bar dataKey="Fraude" fill="var(--color-Fraude)" radius={4} />
              </BarChart>
            </ChartContainer>
          </div>
        </div>

        <div className="flex flex-col w-full justify-top gap-4 pt-[94px] items-start">
          <label
            className="text-2xl font-bold"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            Selecione as matrículas que precisam ter vistoria:
          </label>

          <label
            className="text-center text-sm"
            htmlFor="picture"
            style={{ color: "#757575" }}
          >
            Dados de 20XX
          </label>

          <Table>
            <TableCaption>
              Dados tratados por IA e podem conter erros.
            </TableCaption>
            <TableHeader>
              <TableRow>
                <TableHead
                  className="w-[50px]"
                  style={{
                    fontSize: "16px",
                    fontWeight: "bold",
                    backgroundColor: "#D5E2F1",
                    color: "#072C59",
                  }}
                >
                  Selecionar
                </TableHead>
                <TableHead
                  className="w-[100px]"
                  style={{
                    fontSize: "16px",
                    fontWeight: "bold",
                    backgroundColor: "#D5E2F1",
                    color: "#072C59",
                  }}
                >
                  Categoria
                </TableHead>
                <TableHead
                  style={{
                    fontSize: "16px",
                    fontWeight: "bold",
                    backgroundColor: "#D5E2F1",
                    color: "#072C59",
                  }}
                >
                  Média de consumo (m³)
                </TableHead>
                <TableHead
                  style={{
                    fontSize: "16px",
                    fontWeight: "bold",
                    backgroundColor: "#D5E2F1",
                    color: "#072C59",
                  }}
                >
                  Suspeita
                </TableHead>
                <TableHead
                  className="text-right"
                  style={{
                    fontSize: "16px",
                    fontWeight: "bold",
                    backgroundColor: "#D5E2F1",
                    color: "#072C59",
                  }}
                >
                  Resultado
                </TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {Categorias.map((categoria, index) => (
                <TableRow key={index}>
                  <TableCell>
                    <Checkbox />
                  </TableCell>
                  <TableCell className="font-medium">
                    {categoria.Categoria}
                  </TableCell>
                  <TableCell>{categoria.Medconsumo}</TableCell>
                  <TableCell
                    style={{
                      color:
                        parsePercentage(categoria.Probabilidade) >= 60
                          ? "red"
                          : "inherit",
                    }}
                  >
                    {categoria.Probabilidade}
                  </TableCell>
                  <TableCell
                    className="text-right"
                    style={{
                      color:
                        categoria.Resultado === "Fraude" ? "red" : "inherit",
                      fontWeight:
                        categoria.Resultado === "Fraude" ? "bold" : "normal",
                    }}
                  >
                    {categoria.Resultado}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </div>
    </div>
  );
}
