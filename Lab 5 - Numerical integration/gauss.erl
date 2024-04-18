-module(gauss).
-export([result1/0, result2/0]).

fun1(X) -> 1 / (1 + X*X).

fun2(X) -> 1 / (7 + X).

nodes_and_weights(8) -> [
  {-0.96029, 0.101229}, {-0.796667, 0.222381},
  {-0.525532, 0.313707}, {-0.183435, 0.362684},
  {0.183435, 0.362684}, {0.525532, 0.313707},
  {0.796667, 0.222381}, {0.96029, 0.101229}
];
nodes_and_weights(4) -> [
  {-0.861136, 0.347855}, {-0.339981, 0.652145},
  {0.339981, 0.652145}, {0.861136, 0.347855}
].

%% 2 zadanie labolatoryjne
result1() ->
  Summer = fun ({Node, Weight}, Acc) -> Acc + Weight * fun1(Node) end,
  S = lists:foldl(Summer, 0, nodes_and_weights(8)),
  io:format("Quadrature result: ~w   Error: ~w~n", [S, abs(math:pi()/2 - S)]).

%% 2 zadanie domowe
result2() ->
  Summer = fun ({Node, Weight}, Acc) -> Acc + Weight * fun2(Node) end,
  S = lists:foldl(Summer, 0, nodes_and_weights(4)),
  io:format("Quadrature result: ~w   Error: ~w~n", [S, abs(math:log(4/3) - S)]).
