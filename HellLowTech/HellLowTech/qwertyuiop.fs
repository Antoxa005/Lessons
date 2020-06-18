namespace NewLessons

open System
open System.Numerics

module qwertyuiop =

    let readInt() = Console.ReadLine() |> Int32.Parse
    let readInt64() = Console.ReadLine() |> Int64.Parse
    let readBigInteger() = Console.ReadLine() |> BigInteger.Parse
    let readFloat() = Console.ReadLine() |> Double.Parse
    let readBool() = Console.ReadLine() |> Boolean.Parse
    let readGuid() = Console.ReadLine() |> Guid.Parse


    let lesson1 () =
        let n = Console.ReadLine() |> Int32.Parse
        let resuts = [ for _ in 1..(n - 1) -> Console.ReadLine() |> Int32.Parse ]
        let teams = [ for i in 1..n -> i ]

        let getWinner (r, p) =
            match r with 
            | 1 -> fst p
            | 2 -> snd p
            | _ -> failwith "GFUK #1"

        let getAllWinners p r = List.zip p r |> List.map getWinner

        let getPairs x =
            x
            |> List.mapi (fun i e -> i, e)
            |> List.partition (fun (i, _) -> i % 2 = 0)
            ||> List.zip
            |> List.map (fun (a, b) -> snd a, snd b)

        let getRoundResults r t = getPairs t |> getAllWinners r
        
        let getRounds (r : list<'A>) =
            let split x =
                let (a, b) = 
                    x
                    |> List.mapi (fun i e -> i, e)
                    |> List.partition (fun (i, _) -> i < (x.Length + 1) / 2)

                a |> List.map snd, b |> List.map snd

            let rec splitAll acc x =
                match x with 
                | [e] -> [e] :: acc |> List.rev
                | _ -> 
                    let a, b = split x 
                    splitAll (a :: acc) b

            splitAll [] r

        let rounds = getRounds resuts

        let winner =
            rounds
            |> List.fold (fun acc r -> getRoundResults r acc) teams
            |> List.head 

        printfn "The winner is: %A" winner

        0


    let lesson2 () = 
        let m = readInt()
        let w = readInt()
        let h = readInt()

        let countTiles x = 
            match x % m with 
            | 0 -> (x / m) + 1
            | _ -> (x / m) + 2

        let r = (countTiles h) * (countTiles w)
        printfn "%A" r

        0


    let lesson3 () =
        let n = readInt64()
        let a = readInt64()
        let b = readInt64()
        let c = readInt64()

        let x = (a * n + b) / (a + b)

        let getMinTime f =
            let d = c * f + b * (f - 1L)
            let u = c * f + a * (n - f)
            max d u

        let r =
            [ x; x + 1L ]
            |> List.map(fun e -> e, getMinTime e)
            |> List.sortBy snd 
            |> List.head
            |> fst

        printfn "Floor: %A" (int r)

        0


    let lesson4 () =

        let k = readFloat()
        let p = readFloat()
        let s = readFloat()

        let price = k + (k * p / 100.0)
        let result = s / price

        printfn "%A" result

        0


    let lessons =
        [
            "Tournament", lesson1
            "Tiles", lesson2
            "Elevator", lesson3
            "Pens", lesson4
        ]
        |> List.mapi (fun i (s, f) -> i + 1, s, f)


