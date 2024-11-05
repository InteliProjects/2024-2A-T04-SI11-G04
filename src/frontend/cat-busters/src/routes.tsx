import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import App from "./App";
import Upload from "./pages/upload/upload.component";
import { Prefiltro } from "./pages/pre-filtro/pre_filtro.component";
import { Resultado } from "./pages/resultado/resultado";

const router = createBrowserRouter([
  {
    element: <Outlet />,
    children: [
      {
        path: "/",
        element: <App />,
      },
      {
        path: "/upload",
        element: <Upload />,
      },
      {
        path: "/prefiltro",
        element: <Prefiltro />,
      },
      {
        path: "/resultado",
        element: <Resultado />,
      },
    ],
  },
]);
export const BaseRoutes = () => {
  return <RouterProvider router={router} />;
};
