import { arr } from "./mock/menu/MB13401";

export function MB13401(parm) {
  return new Promise((resolve, reject) => {
    let obj = arr[parm.id - 1] || []
    resolve(obj);
  });
}
