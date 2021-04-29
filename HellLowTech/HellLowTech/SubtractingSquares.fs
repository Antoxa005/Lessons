
namespace HellLowTech


open System

module SubtractingSquares =

    let readInt64() = Console.ReadLine() |> Int64.Parse

    type N =
        {
            n : int64
        }

    let calculate n =
        if n % 4L = 0L
        then 
            let k = n / 4L
            let x = k + 1L
            let y = k - 1L

            Some (x, y)
        else 
            if n % 2L = 1L
            then
                let k = (n - 1L) / 2L
                let x = k + 1L
                let y = k

                Some (x, y)
            else None

    let run() =
        let n = readInt64()
        match calculate n with
        | Some (x, y) -> printfn "Yes, %A %A" x y
        | None -> printfn "No"

        0




