import { Button } from "@/components/ui/button";
import Logo from "../../assets/logo.png";
import { UploadIcon } from "@radix-ui/react-icons";
import { useNavigate } from "react-router-dom";

function Upload() {
  const navigate = useNavigate();

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
            Olá, seja bem vindo! Aqui vamos analisar matrículas e categorizá-las
            em “Possíveis fraudes” ou “Íntegras”.
          </label>

          <label
            className="text-center text-xl"
            htmlFor="picture"
            style={{ color: "#072C59" }}
          >
            1. Para começar selecione a base de dados:
          </label>

          <div
            className="flex items-center justify-center h-[30rem] w-[100%] rounded"
            style={{ borderColor: "#072C59", borderWidth: "1px" }}
          >
            <label className="flex flex-col items-center justify-center cursor-pointer">
              <UploadIcon className="w-10 h-10" />
              <span
                className="mt-2 text-lg font-bold"
                style={{ color: "#072C59" }}
              >
                Fazer upload do computador
              </span>

              <input id="file-upload" type="file" className="hidden" />
            </label>
          </div>
          <div className=" w-full flex justify-center">
            <Button
              onClick={() => navigate("/prefiltro")}
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
export default Upload;
