import API from "./api";

export const loadAllModules = async () => {

  const [

    dashboard,

    ueba,

    stream,

    lanl

  ] = await Promise.all([

    API.get("/api/dashboard"),

    API.get("/api/ueba"),

    API.get("/api/stream"),

    API.get("/api/lanl-users")

  ]);

  return {

    dashboard: dashboard.data,

    ueba: ueba.data,

    stream: stream.data,

    lanl: lanl.data

  };
};