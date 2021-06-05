namespace NewLessons

open System
open System.Numerics
open HellLowTech

module qwertyuiop =

    let readInt() = Console.ReadLine() |> Int32.Parse
    let readInt64() = Console.ReadLine() |> Int64.Parse
    let readBigInteger() = Console.ReadLine() |> BigInteger.Parse
    let readFloat() = Console.ReadLine() |> Double.Parse
    let readBool() = Console.ReadLine() |> Boolean.Parse
    let readGuid() = Console.ReadLine() |> Guid.Parse


    let lesson1 () =
        let n = Console.ReadLine() |> Int32.Parse
        let results = [ for _ in 1..(n - 1) -> Console.ReadLine() |> Int32.Parse ]
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

        let rounds = getRounds results

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


    let lesson5 () =

        let x1 = readInt()
        let y1 = readInt()
        let x2 = readInt()
        let y2 = readInt()
        let x = readInt()
        let y = readInt()

        let rules = 
            [
                x <= x1 && y >= y2 , "NW"
                x > x1 && x < x2 && y > y2 , "N"
                x >= x2 && y >= y2 , "NE"
                x > x2 && y > y1 && y < y2 , "E"
                x >= x2 && y <= y1 , "SE"
                x > x1 && x < x2 && y < y1 , "S"
                x <= x1 && y <= y1 , "SW"
                x < x1 && y > y1 && y < y2 , "W"
            ]

        let result = 
            rules 
            |> List.filter fst 
            |> List.head 
            |> snd 

        printf "%s" result



        0


    let lesson6 () =

        let a = readInt()
        let b = readInt()
        let a1 = a % 2
        let b1 = b % 2
        let x = b1 - a1
        match x with 
        | 0 -> 
            let ans = abs (b - a) / 2 
            printfn "%A mins" ans
        | 1 -> 
            let ans = abs (b + 1 - a) / 2
            printfn "%A mins" ans
        | -1 ->
            let ans = abs (b - a - 1) / 2
            printfn "%A mins" ans
        | _ -> printfn "Gulay Vasya zhuy apilky"

        0


    let lesson7 () =

        let s = readInt()
        let n = readInt()
        let w = [for _ in 1..n -> readInt()]
        let (b, s) = 
            w
            |> List.fold (fun (bull, shit) r -> if bull + r <= s then (bull + r, shit) else (bull, shit + r)) (0, 0)
        printfn "Here is your shit!!!"
        printfn "%A\n%A" b s

        0


    let lesson8 () =

        let solve a b c =
            let d = b * b - 4 * a * c
            let w1 = - ((float (b)) + (sqrt((float d))) / (2.0 * (float(a))))
            let w2 = - ((float (b)) - (sqrt((float d))) / (2.0 * (float(a))))
            float w2


        let run() =
            let a = readInt()
            let b = readInt()
            let c = readInt()
            let w1 = solve a b c
            printfn "%A" w1

        0

    let lessons =
        [
            "Tournament", lesson1
            "Tiles", lesson2
            "Elevator", lesson3
            "Pens", lesson4
            "Raft", lesson5
            "Street", lesson6
            "Packing", lesson7
            "Transporting artifacts", TransportingArtifacts.run
            "Square", Square.run
            "SpeedTransport", SpeedTransport.run
            "SubtractingSqares", SubtractingSquares.run
            "QuadraticSolver", lesson8
        ]
        |> List.mapi (fun i (s, f) -> i + 1, s, f)


