(define (accumulate combiner start n term)
 (cond
  ((= n 0) start)
  ((> n 0)
      (define start (combiner start (term n)))
      (accumulate combiner start (- n 1) term)
  )
 )
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (cond
      ((= n 0) start)
      (else
          (define start (combiner start (term n)))
          (accumulate combiner start (- n 1) term)
      )
  )
)

(define-macro (list-of expr for var in seq if filter-fn)
  'YOUR-CODE-HERE
    ;; always x undefined
    ;;(map (lambda (var) expr) (filter (lambda (var) filter-fn) seq))
    (list 'map (list 'lambda (list var) expr)  (list 'filter (list 'lambda (list var) filter-fn) seq))
    ;;(map (lambda (list var) expr) (list (filter (lambda (list var) filter-fn) seq)))
)
;;(list-of (* x x) for x in '(3 4 5) if (odd? x))