-module(gauss).
-export([result/0]).

f(X) -> 1 / (1 + X*X).

nodes_and_weights() -> [
  {-0.96029, 0.101229}, {-0.796667, 0.222381},
  {-0.525532, 0.313707}, {-0.183435, 0.362684},
  {0.183435, 0.362684}, {0.525532, 0.313707},
  {0.796667, 0.222381}, {0.96029, 0.101229}
].

result() ->
  Summer = fun ({Node, Weight}, Acc) -> Acc + Weight * f(Node) end,
  S = lists:foldl(Summer, 0, nodes_and_weights()),
  io:format("Quadrature result: ~w   Error: ~w~n", [S, abs(math:pi()/2 - S)]).
