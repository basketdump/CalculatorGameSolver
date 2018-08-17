
<h3 id="specifications-of-game">Specifications of Game</h3>
<ul>
<li>There is only one correct path</li>
<li>Available operators, number of moves, and starting numbers change with each new game</li>
<li>Let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>m</mi><mo separator="true">,</mo><mi>n</mi><mo>)</mo><mo>=</mo><msup><mi>n</mi><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow><annotation encoding="application/x-tex">f(m,n) = n^{m+1}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">m</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathit">n</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">m</span><span class="mbin mtight">+</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span></span></span></span> be the number of possible paths of operations</li>
</ul>
<h3 id="overarching-ideas">Overarching Ideas</h3>
<ul>
<li>Bruteforce operations</li>
<li>Do not evaluate anymore once we reach goal</li>
<li>Operators need to be well defined, they are not <em>typical</em> math operators
<ul>
<li>Multiplication <em>Ex: 3x meaning 3 * current number</em></li>
<li>Remove digit <em>Ex: &lt;&lt; meaning truncate the last digit of the current number</em></li>
<li>Insert digit <em>Ex: 5 meaning add 5 to the end of the current number</em></li>
</ul>
</li>
</ul>
<h3 id="algorithm-steps">Algorithm Steps</h3>
<ul>
<li>Let <em>m</em> be the max number of moves</li>
<li>Let <em>n</em> be the number of operators available per move</li>
<li>Let <em>o</em> be the available operators</li>
<li>Let <em>g</em> be the goal</li>
<li>Let <em>x</em> be the starting number</li>
<li>Let <em>y</em> be the result</li>
<li>Let <em>p</em> be the possible paths of operations
<ul>
<li>Length of <em>p</em> is <em>m</em></li>
</ul>
</li>
</ul>
<ol>
<li>Generate all possible paths of operations
<ol>
<li><em>p</em> = [[<em>p1</em>], [<em>p2</em>], [<em>p3</em>], [<em>...</em>]]</li>
</ol>
</li>
<li>Loop &amp; execute each <em>p[i]</em> against <em>x</em> until <em>y</em> == <em>g</em></li>
<li>Display <em>p[i]</em></li>
</ol>